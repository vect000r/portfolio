import { useState } from "react";
import { type FormEvent,type ChangeEvent } from "react";

interface ContactFormData {
  name: string;
  email: string;
  message: string;
}

type StatusType = "success" | "error" | null;

export default function Contact() {
  const [formData, setFormData] = useState<ContactFormData>({
    name: "",
    email: "",
    message: "",
  });

  const [status, setStatus] = useState<StatusType>(null);
  const [loading, setLoading] = useState<boolean>(false);

  const handleChange = (
    e: ChangeEvent<HTMLInputElement | HTMLTextAreaElement>
  ) => {
    setFormData({ ...formData, [e.target.name]: e.target.value });
  };

  const handleSubmit = async (e: FormEvent<HTMLFormElement>) => {
    e.preventDefault();
    setLoading(true);
    setStatus(null);

    try {
      const response = await fetch("http://localhost:8000/api/contact/", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify(formData),
      });

      if (response.ok) {
        setStatus("success");
        setFormData({ name: "", email: "", message: "" });
      } else {
        setStatus("error");
      }
    } catch (error) {
      console.error("Error sending message:", error);
      setStatus("error");
    } finally {
      setLoading(false);
    }
  };

  return (
    <section className="contact-section" id="contact">
      <h2 className="section-title">
        <span className="bracket">{'['}</span>CONTACT
        <span className="bracket">{']'}</span>
      </h2>
      <p className="contact-text">$ echo "Let's build something together"</p>

      <form className="contact-form" onSubmit={handleSubmit}>
        <input
          type="text"
          name="name"
          placeholder="Your Name"
          value={formData.name}
          onChange={handleChange}
          required
          className="contact-input"
        />
        <input
          type="email"
          name="email"
          placeholder="Your Email"
          value={formData.email}
          onChange={handleChange}
          required
          className="contact-input"
        />
        <textarea
          name="message"
          placeholder="Your Message"
          value={formData.message}
          onChange={handleChange}
          required
          rows={5}
          className="contact-textarea"
        ></textarea>

        <button type="submit" className="button" disabled={loading}>
          {loading ? "Sending..." : "Send Message"}
        </button>

        {status === "success" && (
          <p className="status-message success">
            ✓ Your message has been sent!
          </p>
        )}
        {status === "error" && (
          <p className="status-message error">
            ✗ Failed to send message. Try again later.
          </p>
        )}
      </form>

      <div className="contact-links">
        <a href="mailto:vectoreddd@email.com" className="contact-link">
          EMAIL
        </a>
        <a href="https://github.com/vect000r" className="contact-link">
          GITHUB
        </a>
        <a href="https://linkedin.com/in/yourusername" className="contact-link">
          LINKEDIN
        </a>
      </div>
    </section>
  );
}
