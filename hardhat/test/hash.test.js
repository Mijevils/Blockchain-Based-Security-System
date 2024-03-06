// MyContract.test.js
// Example test file for MyContract

const { expect } = require("chai");

describe("hash.sol", function () {
    let hash;

    beforeEach(async function () {
        const hash = await ethers.getContractFactory("hash.sol");
        myContract = await MyContract.deploy();
        await myContract.deployed();
    });

    it("should set value", async function () {
        const newValue = 42;
        await myContract.setValue(newValue);
        expect(await myContract.value()).to.equal(newValue);
    });
});
