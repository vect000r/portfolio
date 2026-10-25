import { BrowserRouter as Router, Route, Routes } from "react-router-dom";
import Contact from "./components/Contact";
import Education from "./components/Education";
import Experience from "./components/Experience";
import Footer from "./components/Footer";
import Hero from "./components/Hero";
import ProjectDetail from "./components/ProjectDetail";
import Projects from "./components/Projects";
import Skills from "./components/Skills";
import TerminalHeader from "./components/TerminalHeader";
import "./App.css";

function HomePage() {
  return (
    <>
      <Hero />
      <div className="content-grid">
        <div>
          <Projects />
          <Experience />
        </div>
        <aside className="side-column">
          <Skills />
          <Education />
        </aside>
      </div>
      <Contact />
    </>
  );
}

export default function App() {
  return (
    <Router>
      <TerminalHeader />
      <main className="terminal-content">
        <Routes>
          <Route path="/" element={<HomePage />} />
          <Route path="/projects/:id" element={<ProjectDetail />} />
        </Routes>
      </main>
      <Footer />
    </Router>
  );
}
