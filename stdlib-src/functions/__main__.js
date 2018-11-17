const ejs = require('ejs');
const fs = require('fs');
/**
* A simple "hello world" function
* @param {string} name
* @param {any} jsonip
* @returns {any}
*/
module.exports = (name = 'AIWebSiteGen', jsonip, context, callback) => {
  // return callback(null, jsonip.replace(/\+/g, '').replace(/\\/g, '').replace(/'/g, '\"'))
  jsonip = JSON.parse(jsonip.replace(/\+/g, ' ').replace(/\\/g, '').replace(/'s /g, ' ').replace(/'/g, '\"'));
  
  //let templateName = jsonip.name;
  var contentheader = jsonip.content.header;
  var contentrefurls = jsonip.content.refurls;
  var contentimages = jsonip.content.images;
  var contentmaincontent  = jsonip.content.mainContent;
  var contentfooter = jsonip.content.footer;
  var contentshare = jsonip.content.share;
  
  var positionheader = jsonip.position.navBar;
  var positionrefurls = jsonip.position.refurls;
  var positionshare = jsonip.position.share;
  var positionimages = jsonip.position.images;
  var positionmaincontent  = jsonip.position.mainContent;
  var positionfooter = jsonip.position.footer;

  let templatePath = './templates/bootstrap-template.ejs';
  return ejs.renderFile(
    templatePath,
    {
      contentheader : contentheader,
      contentfooter: contentfooter,
      contentrefurls: contentrefurls,
      contentimages : contentimages,
      contentmaincontent : contentmaincontent,
      contentshare: contentshare,
      
      positionheader: positionheader,
      positionfooter: positionfooter,
      positionmaincontent: positionmaincontent,
      positionrefurls: positionrefurls,
      positionimages: positionimages,
      positionshare: positionshare
      
    },
    {},
    (err, response) => callback(err, new Buffer(response || ''), {'Content-Type': 'text/html'})
  );

};