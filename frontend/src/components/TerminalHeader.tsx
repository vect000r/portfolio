import { useState, useEffect } from 'react';

export default function TerminalHeader() {
  const [typedText, setTypedText] = useState('');
  const [showCursor, setShowCursor] = useState(true);
  const fullText = "vect000r@portfolio:~$";

  useEffect(() => {
    if (typedText.length < fullText.length) {
      const timeout = setTimeout(() => {
        setTypedText(fullText.slice(0, typedText.length + 1));
      }, 100);
      return () => clearTimeout(timeout);
    }
  }, [typedText]);

  useEffect(() => {
    const interval = setInterval(() => {
      setShowCursor(prev => !prev);
    }, 500);
    return () => clearInterval(interval);
  }, []);

  return (
    <header className="terminal-header">
      <div className="terminal-prompt">
        <span className="prompt-text">{typedText}</span>
        <span className={`cursor ${showCursor ? 'visible' : ''}`}>_</span>
      </div>
    </header>
  );
}