const hre = require("hardhat");

async function main() {
  const [deployer] = await hre.ethers.getSigners();

  console.log("Deploying contracts with account:", deployer.address);

  const ExitToken = await hre.ethers.getContractFactory("ExitToken");
  const initialSupply = hre.ethers.utils.parseUnits("1000000", 18); // 1 million tokens

  const exitToken = await ExitToken.deploy(initialSupply);
  await exitToken.deployed();

  console.log("ExitToken deployed to:", exitToken.address);

  const PrivacyModule = await hre.ethers.getContractFactory("PrivacyModule");
  const privacyModule = await PrivacyModule.deploy();
  await privacyModule.deployed();

  console.log("PrivacyModule deployed to:", privacyModule.address);
}

main()
  .then(() => process.exit(0))
  .catch((error) => {
    console.error(error);
    process.exit(1);
  });
