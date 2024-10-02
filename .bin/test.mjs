#!/usr/bin/env zx
const https = require("https");
const cheerio = require("cheerio");
let startup = false;
let empty = false;
let counter = 0;
let mapShown = 0;
let dustbowl = 0;
let badwater = 0;
let turbine = 0;

const badwater_icon = "";
const dustbowl_icon = "";
const turbine_icon = "";

const server_count = async (ip) => {
    return new Promise((resolve, reject) => {
        https
            .get(
                `https://tsarvar.com/en/servers/team-fortress-2/${ip}`,
                function (res) {
                    let html = "";

                    res.on("data", function (data) {
                        html += data;
                    });

                    res.on("end", function () {
                        const $ = cheerio.load(html);

                        const playerCount = $(".srvPage-countCur").text();
                        resolve(playerCount);
                    });
                }
            )
            .on("error", function (err) {
                reject(err);
            });
    });
};
const ruleToDisplay = (maps) => {
    if (maps.length === 1) {
        return `${maps[0].icon} ${maps[0].count}`;
    }
    const mapToDisplay = maps.find((name) => {
        if (maps.length < mapShown) {
            mapShown = 0;
        }
        return name.id > mapShown;
    });

    mapShown = mapToDisplay.id;
    return `${mapToDisplay.icon} ${mapToDisplay.count}`;
};

const display_count = async (server) => {
    const toDisplay = server.filter(
        (map) => map.count >= 10 || (map.map == "turbine" && map.count >= 30)
    );

    if (toDisplay.length == 0) {
        if (!empty) {
            console.log(
                "The servers are empty or not enough people are playing!"
            );
            empty = true;
        }
        return;
    }
    const display = ruleToDisplay(toDisplay);
    fs.writeFileSync("/home/cie/tf2display", `${display}`);
    empty = false;
};

while (true) {
    try {
        if (counter >= 30 || !startup) {
            dustbowl = await server_count("205.178.182.182:27060");
            await sleep(1000);
            badwater = 2;
            await sleep(1000);
            turbine = 4;
            counter = 0;
            startup = true;
        }

        display_count([
            {
                map: "dustbowl",
                count: dustbowl,
                icon: dustbowl_icon,
                id: 1,
            },
            {
                map: "badwater",
                count: badwater,
                icon: badwater_icon,
                id: 2,
            },
            {
                map: "turbine",
                count: turbine,
                icon: turbine_icon,
                id: 3,
            },
        ]);
    } catch (err) {
        console.log("Error:", err);
    }
    counter++;
    await sleep(60000);
}
