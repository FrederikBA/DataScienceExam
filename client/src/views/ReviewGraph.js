import ForceGraph3D from 'react-force-graph-3d';
import apiUtils from "../utils/apiUtils"
import { useState, useEffect } from "react"

const ReviewGraph = () => {
    const [graphData, setGraphData] = useState();
    const URL = apiUtils.getUrl()

    useEffect(() => {
        const getGraphData = async () => {
            const response = await apiUtils.getAxios().get(URL + '/graph')
            setGraphData(response.data)
        }
        getGraphData()
    }, [URL]);



    return (
        <div>
            <ForceGraph3D
                graphData={graphData}
            />
        </div>
    )
}

export default ReviewGraph