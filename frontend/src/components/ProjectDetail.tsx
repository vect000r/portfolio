import { useEffect, useState } from "react";
import { useParams, Link } from "react-router-dom";

interface Project {
  id: number;
  title: string;
  description: string;
  image?: string | null;
  live_url?: string;
  github_url?: string;
}

export default function ProjectDetail() {
  const { id } = useParams<{ id: string }>();
  const [project, setProject] = useState<Project | null>(null);
  const [loading, setLoading] = useState<boolean>(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const fetchProject = async () => {
      try {
        const response = await fetch(`/api/project/${id}/`);
        if (!response.ok) throw new Error("Failed to fetch project");
        const data = await response.json();
        setProject(data);
      } catch (err) {
        console.error(err);
        setError("Could not load project details.");
      } finally {
        setLoading(false);
      }
    };
    fetchProject();
  }, [id]);

  if (loading) return <p className="contact-text">Loading...</p>;
  if (error) return <p className="status-message error">{error}</p>;
  if (!project) return <p className="status-message error">Project not found.</p>;

  return (
    <section className="projects-section" id="project-detail">
      <h2 className="section-title">
        <span className="bracket">{'['}</span>{project.title}
        <span className="bracket">{']'}</span>
      </h2>

      {project.image && (
        <img
          src={project.image}
          alt={project.title}
          className="project-image"
          style={{ maxWidth: "100%", borderRadius: "8px", marginBottom: "1.5rem" }}
        />
      )}

      <p className="project-description">{project.description}</p>

      <div className="contact-links" style={{ marginTop: "2rem" }}>
        {project.live_url && (
          <a href={project.live_url} target="_blank" rel="noopener noreferrer" className="contact-link">
            LIVE DEMO
          </a>
        )}
        {project.github_url && (
          <a href={project.github_url} target="_blank" rel="noopener noreferrer" className="contact-link">
            GITHUB
          </a>
        )}
        <Link to="/#projects" className="contact-link">← BACK</Link>
      </div>
    </section>
  );
}
