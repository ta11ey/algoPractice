const { assertArrayExpression } = require("@babel/types");
const { assert } = require("console");

/**
 *  selection sort
 *  O(n^2)
 */
function sort(array) {
    var bArray = [];
    var O=0;
    var ogArrayLength = array.length

    for (i = 0; i < ogArrayLength; i++ ) {
        var lowestKnownValue = array[0];
        var lowestKnownIndex = array[0];
        array.map((item, I) => {
        if (item < lowestKnownValue) {
            lowestKnownValue = item;
            lowestKnownIndex = I;
        }

        O++
        })
        array.splice(lowestKnownIndex,1);
        bArray.push(lowestKnownValue);
        O++
    }
    console.log(O)
    return {val: bArray, O: O}
};
function binarySearch(sortedArray, find) {
    
};

module.exports = {sort: sort, binarySearch:binarySearch}