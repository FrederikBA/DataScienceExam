import React, { useState } from 'react';
import { Graph } from 'react-d3-graph';
import api from '../utils/apiUtils';

const Neighbors = () => {
    const [input, setInput] = useState('');
    const [graphData, setGraphData] = useState({ nodes: [], links: [] });

    const handleChange = (e) => {
        setInput(e.target.value);
    }

    const handleSubmit = async (e) => {
        e.preventDefault();
        const response = await api.getAxios().post(api.getUrl() + "/neighbors", { input: input });
        if (response.data) {
            // 1. Add the source node to the nodes array.
            const sourceNode = {
                id: input,
                label: input
            };
            const updatedNodes = [...response.data.nodes, sourceNode];

            // 2. Set the state with the updated nodes and links.
            setGraphData({ nodes: updatedNodes, links: response.data.links });
        } else {
            console.error("Recommendations not found in response data:", response.data);
        }
    };


    const graphConfig = {
        nodeHighlightBehavior: true,
        node: {
            color: 'lightblue',
            size: 120,
            highlightStrokeColor: 'blue',
        },
        link: {
            highlightColor: 'lightblue',
        },
    };

    return (
        <div className="center">
            <h1>Neighbors</h1>
            <div className="text-area-div">
                <form className="form-group text-area" onSubmit={handleSubmit}>
                    <textarea
                        value={input}
                        onChange={handleChange}
                        placeholder="Enter movie summary or keywords"
                        className="form-control text-area"
                    />
                    <button className="btn btn-secondary generate-btn" type="submit">Visualize Neighbors</button>
                </form>
            </div>
            <Graph id="graph-id" data={graphData} config={graphConfig} />
        </div>
    )
}

export default Neighbors;
