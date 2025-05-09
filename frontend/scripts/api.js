import { environment } from "../environments/test.environment";

const api_url = environment.api_url;

export async function fetch_data(category) {
  data = [];

  return fetch(`${api_url}get-topics`, {
    method: "GET",
    headers: {
      "Content-Type": "application/json",
    },
  })
    .then((response) => response.json())
    .then((data) => {
      data = data.data;
    })
    .catch((error) => {
      createErrorBox(
        `${category} konnten nicht gefetcht werden! Verbindung zum Server steht?`
      );
      console.error("Error:", error);
    });
}
