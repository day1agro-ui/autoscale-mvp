/**
 * AutoScale API Client
 * Связь между фронтендом AutoScale и AutoScale AI Engine
 */

const AUTOSCALE_API_URL = "https://autoscale-mvp.onrender.com";

async function checkApiHealth() {
    try {
        const response = await fetch(`${AUTOSCALE_API_URL}/health`);
        if (!response.ok) throw new Error(`API error: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("AutoScale API health check failed:", error);
        return null;
    }
}

async function loadCarsFromAPI() {
    try {
        const response = await fetch(`${AUTOSCALE_API_URL}/cars`);
        if (!response.ok) throw new Error(`API error: ${response.status}`);

        const data = await response.json();
        return data.cars || [];
    } catch (error) {
        console.error("Failed to load cars from AutoScale API:", error);
        return [];
    }
}

async function getCarFromAPI(carId) {
    try {
        const response = await fetch(
            `${AUTOSCALE_API_URL}/cars/${carId}`
        );

        if (!response.ok) throw new Error(`API error: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error(`Failed to load car ${carId}:`, error);
        return null;
    }
}

async function compareCarsFromAPI(car1Id, car2Id) {
    try {
        const response = await fetch(
            `${AUTOSCALE_API_URL}/compare?car1_id=${car1Id}&car2_id=${car2Id}`
        );

        if (!response.ok) throw new Error(`API error: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Failed to compare cars through AutoScale API:", error);
        return null;
    }
}

async function getApiInfo() {
    try {
        const response = await fetch(`${AUTOSCALE_API_URL}/api/info`);
        if (!response.ok) throw new Error(`API error: ${response.status}`);
        return await response.json();
    } catch (error) {
        console.error("Failed to load API info:", error);
        return null;
    }
}
