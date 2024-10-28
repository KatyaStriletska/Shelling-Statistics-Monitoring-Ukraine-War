import React, { useState, useEffect } from 'react';
import Header from './Header';
import PlotStatByYear from './PlotStatByYear';
import MapComponent from './MapComponent';
import GraphLaunchedDestroyedComponent from './GraphLaunchedDestroyedComponent';
import GraphLaunchDestrPerCategoryComponent from './GraphLaunchDestrPerCategoryComponent';
import GraphLaunchPlace from './GraphLaunchPlaceComponent';
import WeaponTable from './WeaponTableComponent';
import ArticleComponent from './ArticleComponent';
import './index.css'
import PredictionComponent from './PredictionComponent';

function App() {
  const [launchPlaces, setLaunchPlaces] = useState([])

  const fetchLaunchPlaces = () =>{
    fetch(`http://127.0.0.1:5000/get_launched_place`)
        .then((res) => res.json())
        .then((data) => {
            console.log(launchPlaces)
            setLaunchPlaces(data)

        })
        .catch((err) => console.log("Error fetching categories:", err));
  }
  useEffect(() => {
    fetchLaunchPlaces();
  }, []);

  return (
    <div>
      <Header />
      <br/>
      <ArticleComponent
        text = "The ongoing Russo-Ukrainian War began in February 2014. Following Ukraine's Revolution of Dignity, Russia occupied and annexed Crimea from Ukraine and supported pro-Russian separatists fighting the Ukrainian military in the Donbas War. These first eight years of conflict also included naval incidents and cyberwarfare. In February 2022, Russia launched a full-scale invasion of Ukraine and began occupying more of the country, starting the biggest conflict in Europe since World War II. The war has resulted in a refugee crisis and tens of thousands of deaths. Since the beginning of the full-scale invasion, Russia has launched more than 25,000 ballistic missiles, cruise missiles, guided bombs, surface-to-air missiles, and UAVs against various targets. This extensive use of aerial and missile weaponry has targeted critical infrastructure, civilian areas, and military installations, causing significant destruction and casualties. "
      />
      <div>
        <GraphLaunchedDestroyedComponent
          apiUrl = "http://localhost:5000/graph1"
        />
      </div>
      <ArticleComponent
        text = "The following charts provide a detailed breakdown of the types and categories of weapons used, including ballistic missiles, cruise missiles, guided bombs, surface-to-air missiles, and unmanned aerial vehicles (UAVs). Each chart categorizes these weapons by model and type, offering insight into the distribution and frequency of use behind the choices in the Russian arsenal. This analysis highlights the diversity and intensity of the weapons systems deployed, emphasizing the range of military technologies employed throughout the conflict. To filter the data, please select a year using the buttons below."
      />
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
      <div className='weapon-table-container'>
        <ArticleComponent
          text= "The table below summarizes the main categories and models of weapons that have been observed during the conflict. These include unmanned aerial vehicles (UAVs), ballistic missiles, and cruise missiles. The UAV (unmanned aerial vehicle) category includes various models such as the Shahed-136/131, Orlan-10, Lancet and others used for reconnaissance, targeting and strike operations. Also represented are ballistic and cruise missiles, such as the Iskander-M and X-59/X-69, which are typically used to strike strategically important targets."
        />
        <WeaponTable
          apiUrl = "http://localhost:5000/weapon_table"
        />
      </div>
      <div>
        <ArticleComponent
          text= "This graph shows the total number of launched and destroyed air and missile objects by launch location. The number of objects (missiles, drones, etc.) is plotted on the vertical axis, and the geographic regions and locations from which they were launched are plotted on the horizontal axis. The data shows that certain regions had particularly high activity, which may indicate their importance as launch sites or logistics centers for such operations. The highest peak values are observed in locations such as Primprsko-Akhrtarsk, Kursk oblast, Chauda(Crimea) and Black Sea."
        />
        <GraphLaunchPlace
          apiUrl = "http://localhost:5000/graph_launch_place"
        />

      </div>
      <div>
        <PredictionComponent
          places = {launchPlaces}
          apiUrl = "http://localhost:5000/predictions"
        />
      </div>

      <br></br>
      
      <br></br>
      {/* <MapComponent/> */}
    </div>
  );
}

export default App;
