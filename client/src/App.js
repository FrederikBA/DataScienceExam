import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './components/Header';
import MovieRecommender from './views/MovieRecommender';
import ReviewGraph from './views/ReviewGraph';
import EstimatedEarnings from "./views/EstimatedEarnings";
import Sentiment from "./views/Sentiment";


const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<ReviewGraph />} />
        <Route path="/earnings" element={<EstimatedEarnings />} />
        <Route path="/movie" element={<MovieRecommender />} />
        <Route path="/sentiment" element={<Sentiment />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;