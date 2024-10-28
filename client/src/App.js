import React from 'react';
import Header from './Header';
import PlotStatByYear from './PlotStatByYear';
import MapComponent from './MapComponent';
import GraphLaunchedDestroyedComponent from './GraphLaunchedDestroyedComponent';
import GraphLaunchDestrPerCategoryComponent from './GraphLaunchDestrPerCategoryComponent';
import GraphLaunchPlace from './GraphLaunchPlaceComponent';
import WeaponTable from './WeaponTableComponent';
import PredictionComponent from './PredictionComponent';

function App() {
  return (
    <div>
      <Header />
      <header className="App-header">
      </header>
      <br></br>
      <div>
        <GraphLaunchedDestroyedComponent
          title = "Launched vs Destroyed Missiles"
          apiUrl = "http://localhost:5000/graph1"
        />
      </div>
      <section className='weaponChart'>
        <PlotStatByYear
          apiUrl = "http://localhost:5000/"
        />
       
         
      </section>
     
      <div>
        <GraphLaunchDestrPerCategoryComponent
          apiUrl = "http://localhost:5000/graph2"  
        />
      </div>
      <div>
        <WeaponTable
          apiUrl = "http://localhost:5000/weapon_table"
        />
      </div>
      <div>
        <GraphLaunchPlace
          apiUrl = "http://localhost:5000/graph_launch_place"
        />
      </div>
      <div>
        <PredictionComponent
        apiUrl = "http://localhost:5000/predictions"
        />
      </div>

      <br></br>
      {/* <PlotStatByYear
        title = "Launched vs Destroyed Missiles"
        apiUrl= "http://localhost:5000/graph1"
      /> */}
      <br></br>
      {/* <MapComponent/> */}
    </div>
  );
}

export default App;
