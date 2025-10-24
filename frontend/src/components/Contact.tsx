export default function Contact() {
  return (
    <section className="contact-section" id="contact">
      <h2 className="section-title">
        <span className="bracket">{'['}</span>
        CONTACT
        <span className="bracket">{']'}</span>
      </h2>
      
      <p className="contact-text">
        $ echo "Let's build something together"
      </p>
      
      <div className="contact-links">
        <a href="mailto:vectoreddd@email.com" className="contact-link">
          EMAIL
        </a>
        <a href="https://github.com/vect000r" className="contact-link">
          GITHUB
        </a>
        <a href="https://www.linkedin.com/in/bart%C5%82omiej-galek-864b7b26b/" className="contact-link">
          LINKEDIN
        </a>
      </div>
    </section>
  );
}