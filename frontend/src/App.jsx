import React, { useState } from 'react';
import ReactMarkdown from 'react-markdown';
import './index.css';

function App() {
  const [abstract, setAbstract] = useState('');
  const [loading, setLoading] = useState(false);
  const [report, setReport] = useState(null);
  const [error, setError] = useState(null);

  const handleAnalyze = async () => {
    if (!abstract.trim()) return;
    
    setLoading(true);
    setError(null);
    setReport(null);

    try {
      // Connect to the FastAPI backend
      const response = await fetch('http://127.0.0.1:8000/analyze', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify({ abstract }),
      });

      const data = await response.json();

      if (data.status === 'success') {
        // Handle LangGraph returning a list of dicts or a raw string
        let rawReport = data.report;
        if (typeof rawReport !== 'string') {
          // If it's a list from LangGraph [{type: 'text', text: '...'}]
          rawReport = Array.isArray(rawReport) ? rawReport[0].text : JSON.stringify(rawReport);
        }
        setReport(rawReport);
      } else {
        setError(data.message || 'An error occurred during analysis.');
      }
    } catch (err) {
      setError('Failed to connect to the server. Make sure the FastAPI backend is running!');
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="app-container">
      <div className="glass-panel">
        <h1>AI Novelty Checker</h1>
        <p className="subtitle">Automated Literature Review & Novelty Assessment</p>

        <div className="input-group">
          <textarea
            placeholder="Paste your proposed research abstract, pipeline, or methodology here..."
            value={abstract}
            onChange={(e) => setAbstract(e.target.value)}
            disabled={loading}
          />
          <button onClick={handleAnalyze} disabled={loading || !abstract.trim()}>
            {loading ? (
              <>
                <div className="spinner"></div>
                Agent is thinking...
              </>
            ) : (
              'Analyze Novelty'
            )}
          </button>
        </div>

        {error && (
          <div className="error-message">
            ⚠️ {error}
          </div>
        )}

        {report && (
          <div className="report-container">
            <div className="report-content">
              <ReactMarkdown>{report}</ReactMarkdown>
            </div>
          </div>
        )}
      </div>
    </div>
  );
}

export default App;
