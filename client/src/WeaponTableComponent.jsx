import React, { useState, useEffect } from 'react';

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
    <div>
        <div className='relative flex flex-col w-full h-full overflow-scroll text-gray-700 bg-white shadow-md rounded-xl bg-clip-border'>
            <table className='w-full text-left table-auto min-w-max'>
                <thead>
                    <tr>
                        <th className='p-4 border-b border-blue-gray-100 bg-blue-gray-50'>
                            <p className="block font-sans text-sm antialiased font-normal leading-none text-blue-gray-900 opacity-70">Category</p>
                        </th>
                        <th>Model</th>
                    </tr>
                    
                </thead>
                <tbody>
                    {data.map((item) => (
                        <React.Fragment key={item}>
                            {item.model.map((model, modelIndex) => (
                                <tr key={modelIndex}>
                                    {/* Якщо це перший елемент категорії, відображаємо категорію, інакше — пусте місце */}
                                    <td>{modelIndex === 0 ? item.category : ''}</td>
                                    <td>{model}</td>
                                </tr>
                            ))}
                            {/* <tr>
                                <td rowSpan={item.model.length}>
                                    {item.category}
                                </td>
                                <td>{item.model[0]}</td>
                            </tr>
                            {item.model.slice(1).map((model, modelIndex) => (
                                <tr key={modelIndex}>
                                    <td>{model}</td>
                                </tr>
                            ))} */}
                        </React.Fragment>
                    ))}
                             
                </tbody>
            </table>
        </div>


    </div>
   )
}