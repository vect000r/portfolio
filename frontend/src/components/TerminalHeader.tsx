import { useEffect, useState } from "react";

const prompt = "ml@bartek:~/lab$";

export default function TerminalHeader() {
  const [typedPrompt, setTypedPrompt] = useState("");

  useEffect(() => {
    if (typedPrompt.length === prompt.length) return;
    const timeout = window.setTimeout(
      () => setTypedPrompt(prompt.slice(0, typedPrompt.length + 1)),
      70,
    );
    return () => window.clearTimeout(timeout);
  }, [typedPrompt]);

  return (
    <header className="terminal-header">
      <div className="window-bar terminal-width">
        <div className="window-lights" aria-hidden="true">
          <span className="light light-red" />
          <span className="light light-yellow" />
          <span className="light light-green" />
        </div>
        <p className="window-title">ai-lab.exe</p>
        <p className="window-meta">runtime: online</p>
      </div>
      <div className="terminal-width terminal-nav-row">
        <a className="brand" href="/">
          <span className="brand-symbol">▰</span>
          BARTŁOMIEJ GALEK / AI LAB
        </a>
        <nav aria-label="Primary navigation">
          <a href="#projects">systems</a>
          <a href="#experience">timeline</a>
          <a href="#contact">collaborate</a>
        </nav>
      </div>
      <div className="terminal-width command-line" aria-label="Terminal prompt">
        <span className="prompt-user">{typedPrompt}</span>
        <span className="prompt-command"> cat profile.md</span>
        <span className="prompt-caret">▋</span>
      </div>
    </header>
  );
}
