import { BrowserRouter as Router, Routes, Route } from "react-router-dom";
import TerminalHeader from "./components/TerminalHeader";
import Hero from "./components/Hero";
import Skills from "./components/Skills";
import Projects from "./components/Projects";
import Education from "./components/Education";
import Contact from "./components/Contact";
import Footer from "./components/Footer";
import ProjectDetail from "./components/ProjectDetail"; 
import "./App.css";

export default function App() {
  return (
    <Router>
      <TerminalHeader />

      <main className="terminal-content">
        <Routes>
          {/* Home route  */}
          <Route
            path="/"
            element={
              <>
                <Hero />
                <Skills />
                <Projects />
                <Education />
                <Contact />
              </>
            }
          />

          {/* Project detail route */}
          <Route path="/projects/:id" element={<ProjectDetail />} />
        </Routes>
      </main>

      <Footer />
    </Router>
  );
}
