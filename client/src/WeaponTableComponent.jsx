import React, { useState, useEffect } from 'react';
import './index.css';

export default function WeaponTable({apiUrl}){  
    const [data, setData] = useState([])
    const [loading, setLoading] = useState(true)

    const fetchData = () => {
        fetch(`${apiUrl}`)
            .then((res) => res.json())
            .then((data) => {
                setData(data)
                console.log(data)
                setLoading(false)
            })
            .catch((err) => console.log("Error fetching data:", err))
    }
   useEffect(() => {
    fetchData();
   }, [])

   return (
    <div className="table-container">
        {data.map((item, index) => (
            <table >
                <thead>
                    <tr>
                        <th >Category</th>
                    <th >Model</th>
                </tr>
            </thead>
            <tbody key={`${item.category}-${index}`}>
                    {item.model.map((model, modelIndex) => (
                            <tr key={modelIndex}>
                                <td >{modelIndex === 0 ? item.category : ''}</td>
                                <td>{model}</td>
                            </tr>
                        ))}
                    </tbody>
        </table>
        ))}


        {/* <div className="table-container">
            <table >
                <thead>
                    <tr>
                        <th >
                        Category
                        </th>
                        <th >Model
                        </th>
                    </tr>
                    
                </thead>
               
                    {data.map((item, index) => (
                         <tbody key={`${item.category}-${index}`}>
                            {item.model.map((model, modelIndex) => (
                                <tr key={modelIndex}>
                                    <td >{modelIndex === 0 ? item.category : ''}</td>
                                    <td>{model}</td>
                                </tr>
                            ))}
                        </tbody>
                    ))
                    }
                             
            </table>
        </div> */}
        


    </div>
   )
}