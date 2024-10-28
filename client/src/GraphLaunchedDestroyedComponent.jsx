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
        <div className='label-container'>
            <h1 className='mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-button md:text-5xl lg:text-4xl dark:text-white'>Total launched and destroyed per month in {selectedYear}</h1>
        </div>
        <div className='buttons'> 
            {years.map((year) => (
                <button 
                    key={year}
                    className={`${
                        selectedYear === year
                            ? "custom-button"
                            : "bg-green-button hover:bg-blue-700"
                    } text-light-button font-bold mr-20 py-2 px-14 rounded`}
                    onClick={() => handleYearChange(year)}
                    disabled={selectedYear === year}
                >{year}</button>
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
