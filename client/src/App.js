import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './components/Header';
import MovieRecommender from './views/MovieRecommender';
import ReviewGraph from './views/ReviewGraph';
import EstimatedEarnings from "./views/EstimatedEarnings";
import Recommendations from './views/Recommendations';
import Neighbors from './views/Neighbors';
import Evaluation from './views/Evaluation';
import Sentiment from "./views/Sentiment";


const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<ReviewGraph />} />
        <Route path="/earnings" element={<EstimatedEarnings />} />
        <Route path="/movie" element={<MovieRecommender />} />
        <Route path="/recommendations" element={<Recommendations />} />
        <Route path="/neighbors" element={<Neighbors />} />
        <Route path="/evaluation" element={<Evaluation />} />
        <Route path="/sentiment" element={<Sentiment />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;