export function getHeaders(additional) {
  const dashUserToken = localStorage.getItem(process.env.REACT_APP_TOKEN_KEY);

  let headers = {
    ...additional,
  };

  if (dashUserToken) {
    headers["Authorization"] = `Token ${dashUserToken}`;
  }
  return headers;
}

export const setPageTitle = (title) => {
  const siteName = process.env.REACT_APP_SITE_TITLE;
  if (title) {
    document.title = siteName + " | " + title;
  } else {
    document.title = siteName;
  }
  return true;
};
