import React, { useState, useEffect } from 'react';
import Header from './Header';
import PlotStatByYear from './PlotStatByYear';
import MapComponent from './MapComponent';
import GraphLaunchedDestroyedComponent from './GraphLaunchedDestroyedComponent';
import GraphLaunchDestrPerCategoryComponent from './GraphLaunchDestrPerCategoryComponent';
import GraphLaunchPlace from './GraphLaunchPlaceComponent';
import WeaponTable from './WeaponTableComponent';
import ArticleComponent from './ArticleComponent';
import CivilianDeathsComponent from './CivilianDeathsComponent';
import './index.css'
import PredictionComponent from './PredictionComponent';

function App() {
  const [launchPlaces, setLaunchPlaces] = useState([])

  const fetchLaunchPlaces = () =>{
    fetch(`https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com/get_launched_place`)
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
      <GraphLaunchedDestroyedComponent
        apiUrl = "http://shelling-statistics-monitoring-ukraine-v9i0:5000/graph1"
      />
      <ArticleComponent
        text = "The following charts provide a detailed breakdown of the types and categories of weapons used, including ballistic missiles, cruise missiles, guided bombs, surface-to-air missiles, and unmanned aerial vehicles (UAVs). Each chart categorizes these weapons by model and type, offering insight into the distribution and frequency of use behind the choices in the Russian arsenal. This analysis highlights the diversity and intensity of the weapons systems deployed, emphasizing the range of military technologies employed throughout the conflict. To filter the data, please select a year using the buttons below."
      />
      <section className='weaponChart'>
        <PlotStatByYear
          apiUrl = "https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com"
        />
      </section>
     
      <GraphLaunchDestrPerCategoryComponent
        apiUrl = "https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com/graph2"  
      />
      <ArticleComponent
        text= "The tables below summarize the main categories and models of weapons that have been observed during the conflict. These include unmanned aerial vehicles (UAVs), ballistic missiles, and cruise missiles. The UAV (unmanned aerial vehicle) category includes various models such as the Shahed-136/131, Orlan-10, Lancet and others used for reconnaissance, targeting and strike operations. Also represented are ballistic and cruise missiles, such as the Iskander-M and X-59/X-69, which are typically used to strike strategically important targets."
      />
      <WeaponTable
        apiUrl = "https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com/weapon_table"
      />
  
      <ArticleComponent
         text= "This graph shows the total number of launched and destroyed air and missile objects by launch location. The number of objects (missiles, drones, etc.) is plotted on the vertical axis, and the geographic regions and locations from which they were launched are plotted on the horizontal axis. The data shows that certain regions had particularly high activity, which may indicate their importance as launch sites or logistics centers for such operations. The highest peak values are observed in locations such as Primprsko-Akhrtarsk, Kursk oblast, Chauda(Crimea) and Black Sea."
      />
      <GraphLaunchPlace
        apiUrl = "https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com/graph_launch_place"
      />
      <PredictionComponent
        places = {launchPlaces}
        apiUrl = "https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com/predictions"
      />
      <ArticleComponent 
        text = {`Lately, The Wall Street Journal (WSJ), citing intelligence and undisclosed sources, reported a grim milestone: about one million Ukrainians and Russians have been killed or wounded since the war began. The majority of dead are soldiers on both sides, followed by Ukrainian civilians. According to government figures, in the first half of 2024, three times as many people died in Ukraine as were born, the WSJ reported.<br/> At least <b>10,000 civilians</b>, including more than <b>560 children</b>, have been killed and over 18,500 have been injured since Russia launched its a full-scale armed attack against Ukraine on 24 February 2022, the United Nations Human Rights Monitoring Mission in Ukraine (HRMMU) said today. <br/>“Nearly half of civilian casualties in the last three months have occurred far away from the frontlines. As a result, no place in Ukraine is completely safe,”  said Danielle Bell, who heads the monitoring mission.
          <br/>This ongoing conflict continues to highlight the devastating impact of war on civilians and the need for urgent humanitarian assistance. The data reflects not only the scale of military engagement but also the profound humanitarian crisis that has ensued, urging the international community to respond to the growing needs of affected populations.
          <br/>Below you can view statistics on total civilian casualties and select the year you are interested in.`}/>
      <CivilianDeathsComponent
        apiUrl = "https://shelling-statistics-monitoring-ukraine-v9i0.onrender.com/civilian_deaths"
      />
      <MapComponent/>
    </div>
  );
}

export default App;
