In the GHG emissions table, kg CO2e is a sum of emissions from CO2,  CH4 and N2O. We want to use kgCO2e/mile or km(to be discussed) total, the first column. There are values for diesel and petrol.

There are notes available on each type of car. This could be added as a layer of granularity. I will add these as a separate csv for now.

Question for Lowr - are we only considering scope 3 emissions, i.e. ones that come directly from using the car. This is mainly an issue with electric vehicles, whose emissions come from geenrating the electricity. This information is available. Need to make it clear that this dataset its for scope 3 emissions.

# List of factors to get
## Passenger vehicles: cars by market segment and size, motorbikes by engine size.
## Electricity for EVs (Not 100% sure as this is scope 2, ask Lowr.)
## Transmission and dustribution (T&D) for EVs.
## Business travel - air
- Users should generally use the ‘including indirect effects of non-CO2 emissions’ factors, which incorporate a 70% increase in CO2 emissions to approximate the indirect impact of non-CO2 emissions from aviation (such as water vapour, contrails and NOx). If the user’s historical data do not include these indirect effects, then they should rebaseline their historical dataset to include the effect going forward. However, users should be aware of the significant scientific uncertainty surrounding the quantification of these impacts. If organisations do not wish to include the indirect effects, then they should continue to select the ‘Direct effects from CO2, CH4 and N2O emissions only’ factors.
## Business travel - sea
## Business travel - taxis, bus, rail
- Users should be mindful of the difference between vehicle km conversion factors and passenger km conversion factors. Vehicle km conversion factors should be applied to a whole vehicle (such as a car or taxi) being used for business purposes. Passenger km factors should be used when single passengers are travelling by means of mass transport (such as by train ) and the aim is to report emissions on a single-person basis, not account for the whole vehicle.