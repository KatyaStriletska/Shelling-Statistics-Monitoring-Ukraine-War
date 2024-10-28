import React, { useState, useEffect } from 'react';
import "./index.css";
export default function PredictionComponent({places, apiUrl}){
    const [selectedYear, setSelectedYear] = useState(2022)
    const [selectedPlace, setSelectedPlace] = useState("Black Sea")
    const [selectedLaunched, setSelectedLaunched] = useState(5)
    const [loading, setLoading] = useState(true)
    const [result, setResult] = useState ([])
    const years = [2022, 2023, 2024];

    const fetchPred = (year, place, launched) =>{
        fetch(`${apiUrl}?year=${year}&place=${place}&launched=${launched}`)
            .then((res) => res.json())
            .then((data) => {
                setResult(data)
                setLoading(false)
            })
            .catch((err) => console.log("Error fetching categories:", err));
    }
    useEffect(() => {
        fetchPred(selectedYear, selectedPlace, selectedLaunched)
    }, [selectedYear, selectedPlace, selectedLaunched]);

    return(
        <div >
            <div className='label-container'>
                <h1 className='mb-4 text-4xl font-extrabold leading-none tracking-tight text-green-button md:text-5xl lg:text-4xl dark:text-white'>Prediction of missile attacks</h1>
            </div>
            <div className='pred-result-container article-container'>
                <article>Prediction of missile attacks Based on the available data on missile attacks during the war in Ukraine, this tool will help you analyze what kind of missile can be launched from a certain location and how likely it is to be shot down by air defense systems. You can choose the launch location, number of missiles, and year to get a forecast and better understand which missile models are used most often and their effectiveness</article>
            </div>
            <div className='prediction'>
                
                <div className='form-prediction-container'>
                    <div className='select-place-container'>
                        <label htmlFor="year" className="block mb-2 text-lg font-medium text-dark-green dark:text-white">Select an launch place</label>
                        <select 
                            id="year"
                            value = {selectedYear}
                            onChange={e => setSelectedYear(e.target.value)} 
                            className="mb-4 bg-gray-50 border border-white text-gray-900 text-m rounded-lg focus:ring-blue-5 focus:border-white-500 block w-[300px] p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                            >
                            {years.map((year) => (
                                <option key={year} value={year}>{year}</option>
                            ))}
                        </select>
                    </div>
                    <div className='select-place-container'>
                        <label htmlFor="place" className="block mb-2 text-lg font-medium text-dark-green dark:text-white">Select an option</label>
                        <select 
                            id="place"
                            value = {selectedPlace}
                            onChange={e => setSelectedPlace(e.target.value)} 
                            className="mb-4 bg-gray-50 border border-white text-gray-900 text-m rounded-lg focus:ring-blue-5 focus:border-white-500 block w-[300px] p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                                               >
                            {places.map((place) => (
                                <option key={place} value={place}>{place}</option>
                            ))}
                        </select>
                    </div>
                    <div className='select-launched-container'>
                        <label 
                            htmlFor='launched'
                            className="block mb-2 text-lg font-medium text-dark-green dark:text-white"
                        >Select number of launched rockets:</label>
                        <input type="number"
                                id="launched"
                                min="1"
                                max="10"
                                value={selectedLaunched}
                                onChange={e => setSelectedLaunched(e.target.value)}
                                aria-describedby="helper-text-explanation" 
                                className="mb-4 bg-gray-50 border border-white text-gray-900 text-m rounded-lg focus:ring-blue-5 focus:border-white-500 block w-[300px] p-2.5 dark:bg-gray-700 dark:border-gray-600 dark:placeholder-gray-400 dark:text-white dark:focus:ring-blue-500 dark:focus:border-blue-500" 
                                required 
                        ></input>
                    </div>
                </div>
                <div className='prediction-result-container'>
                    {loading ? (<p>Loading</p>) : (
                        <div>
                            <p>The most likely to be patched is the <b>{result[0].name}</b>.</p> 
                            <p>The probability that it will be shot down : <b>{result[0].probability.toFixed(2)}%</b>.</p>
                        </div>
                    )}
                    
                </div>   
            </div>
            

        {/* </form> */}
    </div>
    )
}