var binarySearch = require('../BinarySearch').binarySearch;
var sort = require('../BinarySearch').sort;
it ('sorts an unsorted array',() => {
var unsorted = [5,2,4,3,1];
var expected = [1,2,3,4,5];
var returned = sort(unsorted)
expect(returned.val).toEqual(expected);
})

it('binary searches', () => {
    // split the array in half
    //if the X is less than the halved number get rid of upper half
    // is the remaining array length !1? do it again.
})
