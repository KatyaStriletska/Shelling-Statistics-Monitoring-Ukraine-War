import React, { useState, useEffect } from 'react';
import Plot from 'react-plotly.js';
import './index.css';
const GraphLaunchDestrPerCategoryComponent = ({apiUrl}) => {
    const [graphData, setGgraphData] = useState([{}]);
    const [selectedYear, setSelectedYear] = useState(2024);
    const [selectedCategory, setSelectedCategory] = useState('UAV')
    const [allCategories, setAllCategories] = useState([])
    const [loading, setLoading] = useState(false);

    const years = [2022, 2023, 2024];
    const fetchGraphData = (year, category) => {
        setLoading(true)
        fetch(`${apiUrl}?year=${year}&category=${category}`)
          .then((res) => res.json())
          .then((data) => {
            setGgraphData(data);
            setLoading(false);  
          })
          .catch((err) => console.error("Error occurred:", err));
    };
    const fetchCategories = (year) =>{
        fetch(`${apiUrl}/getCategories?year=${year}`)
            .then((res) => res.json())
            .then((data) => {
                setAllCategories(data)
            })
            .catch((err) => console.log("Error fetching categories:", err));
    }
    useEffect(() => {
        fetchGraphData(selectedYear, selectedCategory);
        fetchCategories(selectedYear)
    }, [selectedYear, selectedCategory]);
    
    const handleYearChange = (year) => {
        setSelectedYear(year);
    };
    const handleCategoryChange = (category) => {
        setSelectedCategory(category);
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
        <div className='categoriesGraph'>
            {allCategories ? 
            (<div className= "categories">
                {allCategories.map((category) => (
                    <button
                        onClick={() => handleCategoryChange(category)}
                        key= {category}
                        className='bg-green-button text-light-button hover:bg-blue-700 font-bold mb-10 py-2 px-14 rounded'

                    >{category}</button>
                ))}
            </div>) : (<p>Loading...</p>)}
                {loading ? (<p>Loading...</p>) : (
                    graphData ? (
                        // <div className='graphByCategory'>
                        <Plot
                            
                            data = {graphData.data}
                            layout={graphData.layout}
                            style={{ width: "100%", height: "600px" }}
                        />
                        // </div>
                    ) : ( <p>No data available</p> )
                )}
            
        </div>

        
    </div>)
}
export default GraphLaunchDestrPerCategoryComponent;
