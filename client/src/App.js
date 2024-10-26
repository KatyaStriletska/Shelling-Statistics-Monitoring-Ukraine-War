import React from 'react';
import Header from './Header';
import PlotStatByYear from './PlotStatByYear';

function App() {
  return (
    <div>
      <Header />
      <header className="App-header">
      </header>
      <br></br>
      <PlotStatByYear
        title = "Launched vs Destroyed Missiles"
        apiUrl= "http://localhost:5000/graph1"
      />
    </div>
  );
}

export default App;
