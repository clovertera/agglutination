import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import { decomposeWord } from './api';
import Dropdown from 'react-dropdown';
import WordAnalysis from "./components/WordAnalysis";
import "bootstrap/dist/css/bootstrap.min.css";

function App() {
    const [word, setWord] = useState('');
    interface Features {
        [key: string]: string | string[];
    }
    interface Interpretation {
        zemberek_analysis: string;
        morphological_features: Features[];
    }
    interface AnalysisData {
        word: string;
        interpretations: Interpretation[];
        language: string;
    }
    const [decomposed, setDecomposed] = useState<AnalysisData | null>(null);

    const languageOptions = [
        'Turkish'
    ]
    // TODO: save for user?
    const defaultLanguage = languageOptions[0];
    const [selectedLanguage, setSelectedLanguage] = useState(defaultLanguage);

    const handleSelectLanguage = (option: string) => {
        setSelectedLanguage(option);
    };

    const handleDecomposition = async () => {
        const result = await decomposeWord(word, selectedLanguage);
        setDecomposed(result);
    };

  return (
      <>
          <header className="header">
          <div className="flexbox-container">
            <a href="https://react.dev" target="_blank">
              <img src={reactLogo} className="logo react" alt="React logo" />
            </a>
            <h1>Agglutination Deconstructor</h1>
          </div>
          </header>
          <div className="flexbox-container">
            <input
                type="text"
                value={word}
                onChange={(e) => setWord(e.target.value)}
                  style={{
                      width: '100%',
                      height: '3rem'
                  }}
              />
              <Dropdown
                  options={languageOptions}
                  onChange={(option) => handleSelectLanguage(option.value)}
                  value={selectedLanguage}
                  placeholder="Language"
              />
          </div>
          <button onClick={handleDecomposition}>Decompose Word</button>

          {decomposed && (
              <div>
                  <h3>Decomposed Word:</h3>
                  {decomposed.interpretations.map((interpretation, index) => (
                      <WordAnalysis key={index} title={decomposed.word} list={decomposed.interpretations[index].morphological_features} />
                  ))}
              </div>
          )}
    </>
  )
}

export default App
