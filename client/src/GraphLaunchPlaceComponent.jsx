import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';

export default function GraphLaunchPlace({apiUrl}){

  const [graphData, setGgraphData] = useState([{}]);
  const [loading, setLoading] = useState(false);

    const fetchGraphData = () => {
        fetch(`${apiUrl}`)
          .then((res) => res.json())
          .then((data) => {
            setGgraphData(data);
            setLoading(false);  
          })
          .catch((err) => console.error("Error occurred:", err));
    };
    
    useEffect(() => {
        fetchGraphData();
    }, []);

    return (
    <div>
        <div className='label-container'>
            <h1 className='mb-4 mt-10 text-4xl font-extrabold leading-none tracking-tight text-green-button md:text-5xl lg:text-4xl dark:text-white'>Total launched and destroyed by launch place</h1>
        </div>
            {loading ? (<p>Loading...</p>) : (
                graphData ? (
                   
                    <Plot
                        data = {graphData.data}
                        layout={graphData.layout}
                        style={{ width: "100%", height: "600px" }}
                    />
                    
                ) : ( <p>No data available</p> )
            )}

        
    </div>)
}