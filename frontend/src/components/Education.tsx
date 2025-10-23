import { useEffect, useState } from "react";

interface EducationItem {
  id: number;
  school: string;
  degree: string;
  field_of_study?: string;
  start_date: string;
  end_date?: string | null;
  description?: string;
  location?: string;
  gpa?: string;
  years_display?: string;
}

export default function Education() {
  const [education, setEducation] = useState<EducationItem[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchEducation = async () => {
      try {
        const response = await fetch("/api/education/");
        if (!response.ok) throw new Error("Failed to fetch education");
        const data = await response.json();
        setEducation(data);
      } catch (err) {
        console.error(err);
        setError("Could not load education data.");
      } finally {
        setLoading(false);
      }
    };

    fetchEducation();
  }, []);

  if (loading) return <p className="contact-text">Loading...</p>;
  if (error) return <p className="status-message error">{error}</p>;

  return (
    <section className="education-section" id="education">
      <h2 className="section-title">
        <span className="bracket">{'['}</span>EDUCATION<span className="bracket">{']'}</span>
      </h2>

      {education.map((edu, index) => (
        <div key={edu.id} className="education-item">
          <div className="edu-number">
            [{String(index + 1).padStart(2, "0")}]
          </div>
          <div className="edu-content">
            <h3>
              {edu.degree}
              {edu.field_of_study ? ` • ${edu.field_of_study}` : ""}
            </h3>
            <p>
              {edu.school}
              {edu.location ? ` • ${edu.location}` : ""} •{" "}
              {edu.years_display
                ? edu.years_display
                : `${new Date(edu.start_date).getFullYear()} - ${
                    edu.end_date
                      ? new Date(edu.end_date).getFullYear()
                      : "Present"
                  }`}
            </p>
            {edu.gpa && <p>GPA: {edu.gpa}</p>}
            {edu.description && (
              <p className="project-description">{edu.description}</p>
            )}
          </div>
        </div>
      ))}
    </section>
  );
}
