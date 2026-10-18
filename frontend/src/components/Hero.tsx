export default function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-copy">
        <p className="eyebrow">AI/ML ENGINEER / RETRIEVAL SYSTEMS / NLP</p>
        <h1>
          Making AI
          <br />
          <span>useful.</span>
        </h1>
        <p className="hero-description">
          I&apos;m Bartek, an AI/ML developer focused on turning language models
          into reliable products — grounded in your data, measured in production,
          and built for people.
        </p>
        <div className="hero-actions">
          <a className="terminal-button terminal-button-primary" href="#projects">
            ./inspect-systems <span>↘</span>
          </a>
          <a className="terminal-button" href="#contact">
            ./start-collaboration <span>↗</span>
          </a>
        </div>
      </div>
      <div className="hero-console" aria-label="Developer profile">
        <div className="console-heading">
          <span>model_card.json</span>
          <span>01 / 04</span>
        </div>
        <pre>{`const engineer = {
  name: "Bartek",
  focus: ["RAG", "NLP", "MCP servers"],
  tools: ["Python", "Elasticsearch", "LangChain"],
  vector_store: "Elasticsearch",
  integrations: ["MCP"],
  status: "inference-ready"
};`}</pre>
        <div className="console-footer">
          <span>UTF-8</span>
          <span>Ln 09, Col 01</span>
        </div>
      </div>
    </section>
  );
}
