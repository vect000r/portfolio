export default function Hero() {
  return (
    <section className="hero-section">
      <h1>HI, I'M BARTEK</h1>
      <p className="subtitle">
        <span className="bracket">{'>'}</span> DEVELOPER
      </p>
      <p className="description">
        Building with modern technologies.
        Passionate about clean code and user experience.
      </p>
      <div className="cta-buttons">
        <button className="button" onClick={() => window.location.href = '#projects'}>
          VIEW_PROJECTS
        </button>
        <button className="button" onClick={() => window.location.href = '#contact'}>
          CONTACT_ME
        </button>
      </div>
    </section>
  );
}