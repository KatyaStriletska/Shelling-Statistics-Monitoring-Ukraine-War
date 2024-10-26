import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import './index.css';
const PlotStatByYear = ({graphTitle, apiUrl}) => {
    const [graph, setGraph] = useState([{}]);
    const [selectedYear, setSelectedYear] = useState(2024);
    const [loading, setLoading] = useState(false);
    const years = [2022, 2023, 2024];
    const fetchGraphData = (year) => {
        fetch(`${apiUrl}?year=${year}`)
          .then((res) => res.json())
          .then((data) => {
            setGraph(data);
            setLoading(false);  
          })
          .catch((err) => console.error("Error occurred:", err));
    };
    
    useEffect(() => {
        fetchGraphData(selectedYear);
    }, [selectedYear]);
    
    const handleYearChange = (year) => {
        console.log(`click button ${year}`)
        setLoading(true);
        setSelectedYear(year);
    };

    return (
    <div>
        <h3>{graphTitle}</h3>
        <div> 
            {years.map((year) => (
                <button 
                    key={year} 
                    className="bg-green-button text-white hover:bg-blue-700 text-white font-bold mr-20 py-2 px-4 rounded"
                    onClick={() => handleYearChange(year)}>
                    {year}
                </button>
            ))}
        </div>
        {loading ? (<p>LOADING</p>) :(
        graph.data ? (
            <Plot
                data={graph.data}    
                layout={graph.layout}
                style={{ width: "100%", height: "600px" }}
            />
        ) : ( <p>No data available</p> )
        )}
    </div>)
}
export default PlotStatByYear;
