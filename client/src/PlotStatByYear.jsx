import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import './index.css';

const PlotStatByYear = ({apiUrl}) => {
    const [chartModel, setChartModel] = useState([{}]);
    const [chartCategory, setChartCategory] = useState([{}]);

    const [selectedYear, setSelectedYear] = useState(2024);
    const [loadingModel, setLoadingModel] = useState(false);
    const [loadingCategory, setLoadingCategory] = useState(false);

    const years = [2022, 2023, 2024];

    const fetchGraphData = (year) => {
        fetch(`${apiUrl}/chartModel?year=${year}`)
          .then((res) => res.json())
          .then((data) => {
            setChartModel(data);
            setLoadingModel(false);  
          })
          .catch((err) => console.error("Error occurred:", err));
        fetch(`${apiUrl}/chartCategory?year=${year}`)
          .then((res) => res.json())
          .then((data) => {
            setChartCategory(data);
            setLoadingCategory(false);  
          })
          .catch((err) => console.error("Error occurred:", err));
    };
    
    useEffect(() => {
        fetchGraphData(selectedYear);
    }, [selectedYear]);
    
    const handleYearChange = (year) => {
        setLoadingCategory(true);
        setLoadingModel(true);
        setSelectedYear(year);
    };

    return (
    <div>
        <div className='label-container'>
            <h1 className='mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-button md:text-5xl lg:text-4xl dark:text-white'>
                The most common categories of weapons and weapons by year
            </h1>
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
                    disabled={selectedYear === year}>
                    {year}
                </button>
            ))}
        </div>
        <div className='weaponCharts'>
            {loadingModel ? (<p>Loading...</p>) : (
                chartModel ? (
                    <div  className='chart'>
                    <Plot 
                        data = {chartModel.data}
                        layout={chartModel.layout}
                    />
                    </div>
                ) : ( <p>No data available</p> )
            )}
            {loadingCategory ? (<p>Loading...</p>) : (
                chartCategory ? (
                    <div className='chart'>
                    <Plot
                        data = {chartCategory.data}
                        layout={chartCategory.layout}
                    />
                    </div>
                ) : ( <p>No data available</p> )
            )}

        </div>

        
    </div>)
}
export default PlotStatByYear;
