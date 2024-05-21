import Routes from "./Routes/Routes";
import "./App.css";
import { useSelector } from "react-redux";
import FullScreenLoading from "./components/Loader/FullScreenLoading";

const App = () => {
  const auth = useSelector((state) => state.auth);

  if (auth.loading)
    return <FullScreenLoading />;

  return <Routes />
};

export default App;
