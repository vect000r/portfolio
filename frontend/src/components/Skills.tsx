import { useState, useEffect } from "react";

interface Skill {
  id: number;
  name: string;
  order: number;
}

export default function Skills() {
  const [skills, setSkills] = useState<Skill[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchSkills = async () => {
      try {
        const response = await fetch("/api/skill/");
        if (!response.ok) {
          throw new Error("Failed to fetch skills");
        }
        const data: Skill[] = await response.json();
        setSkills(data);
      } catch (err) {
        setError(err instanceof Error ? err.message : "Unknown error");
      } finally {
        setLoading(false);
      }
    };

    fetchSkills();
  }, []);

  if (loading) return <p>Loading skills...</p>;
  if (error) return <p>Error: {error}</p>;

  return (
    <section className="skills-section">
      <h2 className="section-title">
        <span className="bracket">{'['}</span>SKILLS<span className="bracket">{']'}</span>
      </h2>
      <div className="skills-grid">
        {skills.map((skill) => (
          <div key={skill.id} className="skill-tag">
            {skill.name}
          </div>
        ))}
      </div>
    </section>
  );
}
