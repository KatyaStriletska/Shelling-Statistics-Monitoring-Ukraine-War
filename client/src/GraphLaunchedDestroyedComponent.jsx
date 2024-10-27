import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import './index.css';
const GraphLaunchedDestroyedComponent = ({apiUrl}) => {
    const [graphData, setGgraphData] = useState([{}]);
    const [selectedYear, setSelectedYear] = useState(2024);
    const [loading, setLoading] = useState(false);

    const years = [2022, 2023, 2024];

    const fetchGraphData = (year) => {
        fetch(`${apiUrl}?year=${year}`)
          .then((res) => res.json())
          .then((data) => {
            setGgraphData(data);
            setLoading(false);  
          })
          .catch((err) => console.error("Error occurred:", err));
    };
    
    useEffect(() => {
        fetchGraphData(selectedYear);
    }, [selectedYear]);
    
    const handleYearChange = (year) => {
        setLoading(true);
        setSelectedYear(year);
    };

    return (
    <div>
        <h1>SOME TITLE</h1>
        <div className='buttons'> 
            {years.map((year) => (
                <button 
                    key={year} 
                    className="bg-green-button text-light-button hover:bg-blue-700 font-bold mr-20 py-2 px-14 rounded"
                    onClick={() => handleYearChange(year)}>
                    {year}
                </button>
            ))}
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
export default GraphLaunchedDestroyedComponent;
