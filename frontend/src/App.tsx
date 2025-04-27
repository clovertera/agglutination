import { useState } from 'react';
import reactLogo from './assets/react.svg';
import './App.css';
import './index.css';
import { decomposeWord } from './api';
import Button from 'react-bootstrap/Button';
import Dropdown from 'react-bootstrap/Dropdown';
import WordAnalysis from "./components/WordAnalysis";

function App() {
    const [showDecomposed, setShowDecomposed] = useState(false);
    const [word, setWord] = useState('');
    let result: AnalysisData | null = null;
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
        if (word === '' || word === decomposed?.word) {
            return;
        }
        result = await decomposeWord(word, selectedLanguage);
    };

  // TODO: improve preloading logic for efficiency?
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

          <div className="flexbox-container"
              style={{
                  width: '90vh',
                  display: 'flex',
                  flexDirection: 'column',
                  height: '80vh',
                  alignItems: 'center',
              }}>
              <div className="flexbox-container"
                  style={{
                      width: '100%',
                      padding: '20px',
                      alignContent: 'center',
                  }}>


                <Dropdown>
                    <Dropdown.Toggle
                        variant="primary"
                        id="dropdown-basic"
                        style={{
                            backgroundColor: "#ad3434",
                            color: "white",
                            border: "none",
                            height: "100%"
                        }}
                    >
                        {defaultLanguage}
                    </Dropdown.Toggle>
                    <Dropdown.Menu>
                        {languageOptions.map((option, index) => (
                            <Dropdown.Item onClick={() => handleSelectLanguage(option)} key={index}>{option}</Dropdown.Item>
                        ))}
                    </Dropdown.Menu>
                </Dropdown>

                <input
                    type="text"
                    value={word}
                    onChange={(e) => setWord(e.target.value)}
                    style={{
                        width: '100%',
                        height: '3rem'
                    }}
                  />


                  <Button onMouseEnter={handleDecomposition}
                      onClick={() => {
                          if (word !== decomposed?.word) {
                              setDecomposed(result);
                              setShowDecomposed(true);
                          }
                      }}>
                      🔎︎
                  </Button>
              </div>

              {decomposed && showDecomposed && (
                  <div>
                      {decomposed.interpretations.map((interpretation, index) => (
                          <WordAnalysis key={index} title={decomposed.word} list={decomposed.interpretations[index].morphological_features} />
                      ))}
                  </div>
              )}
          </div>

    </>
  )
}

export default App
