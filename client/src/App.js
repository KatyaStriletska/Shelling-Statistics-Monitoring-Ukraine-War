import React from 'react';
import Header from './Header';
import PlotStatByYear from './PlotStatByYear';
import MapComponent from './MapComponent';

function App() {
  return (
    <div>
      <Header />
      <header className="App-header">
      </header>
      <br></br>
      <PlotStatByYear
        title = "Launched vs Destroyed Missiles"
        apiUrl= "http://localhost:5000/graph2"
      />
      <br></br>
      <PlotStatByYear
        title = "Launched vs Destroyed Missiles"
        apiUrl= "http://localhost:5000/graph1"
      />
      <br></br>
      {/* <MapComponent/> */}
    </div>
  );
}

export default App;
