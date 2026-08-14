import os
import requests
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("AVIATION_API_KEY")


def _normalize_airline(name: str) -> str:
    if not name:
        return "Unknown"
    s = str(name).strip()
    # Remove common noise like parenthetical codes and excessive whitespace
    if "(" in s:
        s = s.split("(")[0].strip()
    s = " ".join(s.split())
    return s


def search_flights_structured(query):
    """Return a list of structured flight dicts. Each dict contains keys:
    `airline_name`, `departure_airport`, `arrival_airport`, `status`.
    """
    url = "http://api.aviationstack.com/v1/flights"

    params = {
        "access_key": API_KEY,
        "limit": 5
    }
    try:
        response = requests.get(url, params=params, timeout=8)
        response.raise_for_status()
        data = response.json()
    except Exception as e:
        print(f"flight search error: {e}")
        return []

    out = []
    if "data" in data:
        for flight in data["data"][:5]:
            airline_raw = flight.get("airline", {}).get("name")
            airline = _normalize_airline(airline_raw)

            departure = (
                flight.get("departure", {}).get("airport")
                or flight.get("departure", {}).get("iata")
                or "Unknown"
            )

            arrival = (
                flight.get("arrival", {}).get("airport")
                or flight.get("arrival", {}).get("iata")
                or "Unknown"
            )

            status = flight.get("flight_status") or "Unknown"

            out.append({
                "airline_name": airline,
                "departure_airport": departure,
                "arrival_airport": arrival,
                "status": status,
            })

    return out


def search_flights(query):
    """Backward-compatible textual summary of flights (keeps old API)."""
    items = search_flights_structured(query)
    if not items:
        return "No flight data available."
    lines = []
    for it in items:
        lines.append(
            f"Airline: {it.get('airline_name')} Departure: {it.get('departure_airport')} Arrival: {it.get('arrival_airport')} Status: {it.get('status')}"
        )
    return "\n".join(lines)