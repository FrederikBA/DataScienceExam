import { BrowserRouter, Routes, Route } from "react-router-dom";
import Header from './components/Header';
import Movie_recommender from './views/Movie_recommender';
import Two from './views/Two';
import Recommendations from './views/Recommendations';
import Neighbors from './views/Neighbors';
import Evaluation from './views/Evaluation';


const App = () => {

  return (
    <BrowserRouter>
      <Header />
      <Routes>
        <Route path="/" element={<Two />} />
        <Route path="/movie" element={<Movie_recommender />} />
        <Route path="/recommendations" element={<Recommendations />} />
        <Route path="/neighbors" element={<Neighbors />} />
        <Route path="/evaluation" element={<Evaluation />} />
      </Routes>
    </BrowserRouter>
  );
}

export default App;