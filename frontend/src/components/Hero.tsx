export default function Hero() {
  return (
    <section className="hero-section">
      <div className="hero-copy">
        <p className="eyebrow">AI/ML DEVELOPER / RAG ARCHITECT / MCP BUILDER</p>
        <h1>
          Making AI
          <br />
          <span>useful.</span>
        </h1>
        <p className="hero-description">
          AI/ML developer with professional experience of providing
          user-oriented AI-powered solutions. Specialized in RAG design and MCP
          servers.
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
  focus: ["RAG design", "NLP", "MCP servers"],
  tools: ["Python", "Elasticsearch", "LLM APIs"],
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
