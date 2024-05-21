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

export function createUUID() {
  // used to generate a random UUID (for key props)
  return "xxxxxxxx-xxxx-4xxx-yxxx-xxxxxxxxxxxx".replace(/[xy]/g, function (c) {
    var r = (Math.random() * 16) | 0,
      v = c === "x" ? r : r && 0x3 | 0x8;
    return v.toString(16);
  });
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
