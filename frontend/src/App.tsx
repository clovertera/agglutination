import { useState } from 'react'
import reactLogo from './assets/react.svg'
import viteLogo from '/vite.svg'
import './App.css'
import { decomposeWord } from './api';

function App() {
    const [count, setCount] = useState(0)
    const [word, setWord] = useState('');
    const [decomposed, setDecomposed] = useState(null);

    const handleDecomposition = async () => {
        const result = await decomposeWord(word);
        setDecomposed(result);
    };

  return (
    <>
      <div>
        <a href="https://vite.dev" target="_blank">
          <img src={viteLogo} className="logo" alt="Vite logo" />
        </a>
        <a href="https://react.dev" target="_blank">
          <img src={reactLogo} className="logo react" alt="React logo" />
        </a>
      </div>
          <h1>Vite + React</h1>
          <input
              type="text"
              value={word}
              onChange={(e) => setWord(e.target.value)}
          />
          <button onClick={handleDecomposition}>Decompose Word</button>

          {decomposed && (
              <div>
                  <h3>Decomposed Word:</h3>
                  <pre>{JSON.stringify(decomposed, null, 2)}</pre>
              </div>
          ) }
      <div className="card">
        <button onClick={() => setCount((count) => count + 1)}>
          count is {count}
        </button>
        <p>
          Edit <code>src/App.tsx</code> and save to test HMR
        </p>
      </div>
      <p className="read-the-docs">
        Click on the Vite and React logos to learn more
      </p>
    </>
  )
}

export default App