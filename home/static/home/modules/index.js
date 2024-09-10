import {
    displayNearbyStores,
    setStoreNavigation,
} from './stores.js';

import {
    displayNearbyWishlists,
    displayMyRequests,
    displayMyTrips,
    createWishlist,
    updateWishlistStatus,
} from './wishlists.js';

import {
    addMap,
    addGeocoder,
} from './map.js';

export const USERNAME = document.body.getAttribute("data-username");

let MAP = {};

MAP = addMap();

geocoder = addGeocoder(MAP, (data) => {
    Promise.all([
        displayNearbyStores(MAP, data.result.center[1], data.result.center[0]),
        displayNearbyWishlists(data.result.center[1], data.result.center[0]),
        displayMyRequests(data.result.center[1], data.result.center[0]),
        displayMyTrips(data.result.center[1], data.result.center[0])
    ]).then(([storesGeoJson]) => {
        setStoreNavigation(MAP, storesGeoJson);
    });
  
});
