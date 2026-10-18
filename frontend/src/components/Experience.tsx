import { useEffect, useState } from "react";

interface ExperienceItem {
  id: number;
  company: string;
  role: string;
  description?: string;
  start_date: string;
  end_date?: string | null;
  years_display?: string;
  technologies?: string[];
  location?: string;
}

function formatDate(date: string) {
  return new Intl.DateTimeFormat("en", {
    month: "short",
    year: "numeric",
  }).format(new Date(`${date}T00:00:00`));
}

export default function Experience() {
  const [experience, setExperience] = useState<ExperienceItem[]>([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState<string | null>(null);

  useEffect(() => {
    const controller = new AbortController();

    fetch("/api/experience/", { signal: controller.signal })
      .then((response) => {
        if (!response.ok) throw new Error("Failed to fetch experience");
        return response.json() as Promise<ExperienceItem[]>;
      })
      .then(setExperience)
      .catch((reason: unknown) => {
        if (reason instanceof DOMException && reason.name === "AbortError") return;
        setError("Could not load experience data.");
      })
      .finally(() => setLoading(false));

    return () => controller.abort();
  }, []);

  return (
    <section className="experience-section" id="experience">
      <h2 className="section-title">
        <span className="bracket">[</span>EXPERIENCE<span className="bracket">]</span>
      </h2>

      {loading && <p className="status-message">Loading experience...</p>}
      {error && <p className="status-message error">{error}</p>}
      {!loading && !error && experience.length === 0 && (
        <p className="status-message">Experience will be added soon.</p>
      )}

      <div className="experience-list">
        {experience.map((item, index) => (
          <article className="experience-item" key={item.id}>
            <div className="experience-marker">[{String(index + 1).padStart(2, "0")}]</div>
            <div className="experience-content">
              <div className="experience-heading">
                <div>
                  <h3>{item.role}</h3>
                  <p className="experience-company">{item.company}</p>
                </div>
                <p className="experience-dates">
                  {item.years_display ??
                    `${formatDate(item.start_date)} – ${
                      item.end_date ? formatDate(item.end_date) : "Present"
                    }`}
                </p>
              </div>
              {item.location && <p className="experience-location">{item.location}</p>}
              {item.description && <p className="experience-description">{item.description}</p>}
              {item.technologies && item.technologies.length > 0 && (
                <ul className="technology-list" aria-label="Technologies used">
                  {item.technologies.map((technology) => (
                    <li key={technology}>{technology}</li>
                  ))}
                </ul>
              )}
            </div>
          </article>
        ))}
      </div>
    </section>
  );
}
