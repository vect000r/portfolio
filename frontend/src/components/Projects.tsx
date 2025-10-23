import { useEffect, useState } from "react";
import { useNavigate } from "react-router-dom";

interface Project {
  id: number;
  title: string;
  short_description: string;
  description: string;
  image?: string | null;
  live_url?: string;
  github_url?: string;
}

export default function Projects() {
  const [projects, setProjects] = useState<Project[]>([]);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  const navigate = useNavigate();

  useEffect(() => {
    const fetchProjects = async () => {
      try {
        const response = await fetch("/api/project/");
        if (!response.ok) throw new Error("Failed to fetch projects");
        const data = await response.json();
        setProjects(data);
      } catch (err) {
        console.error(err);
        setError("Could not load projects.");
      } finally {
        setLoading(false);
      }
    };
    fetchProjects();
  }, []);

  if (loading) {
    return <p className="contact-text">Loading projects...</p>;
  }

  if (error) {
    return <p className="status-message error">{error}</p>;
  }

  return (
    <section className="projects-section" id="projects">
      <h2 className="section-title">
        <span className="bracket">{'['}</span>PROJECTS
        <span className="bracket">{']'}</span>
      </h2>

      <div className="projects-list">
        {projects.map((project, index) => (
          <div
            key={project.id}
            className="project-item"
            onClick={() => navigate(`/projects/${project.id}`)}
            style={{ cursor: "pointer" }}
          >
            <div className="project-number">
              [{String(index + 1).padStart(2, "0")}]
            </div>
            <div className="project-content">
              <h3 className="project-title">{project.title}</h3>
              <p className="project-description">
                {project.short_description || project.description}
              </p>
            </div>
            <button className="project-arrow">→</button>
          </div>
        ))}
      </div>
    </section>
  );
}
