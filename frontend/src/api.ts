// frontend/src/api.ts

import axios from 'axios';

// react helper func to call django backend api
export const decomposeWord = async (word: string, language: string) => {
    try {
        // make a GET request to backend API
        const response = await axios.get(`http://127.0.0.1:8000/api/decompose/`, {
            // the word to decompose is passed as a query param
            params: { word, language },
        });

        // response will be decomposed word in JSON format
        console.log(response.data);
        return response.data;
    } catch (error) {
        console.error("Error!", error);
        return null;
    }
};