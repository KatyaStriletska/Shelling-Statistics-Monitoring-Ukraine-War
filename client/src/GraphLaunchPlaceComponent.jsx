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
        <h1>SOME TITLE</h1>
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