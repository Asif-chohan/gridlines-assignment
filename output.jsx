import React from 'react';

const SlideComponent = () => {
  return (
    <div style={{ position: 'relative', width: '100%', height: '100%', backgroundColor: '#fff', paddingBottom: '30px' }}>
      <div key='0' style={{position: "absolute", left: "65.62009841653543px", top: "49.822657595275594px", width: "158.2568222047244px", height: "51.699923243307076px", transform: "rotate(0deg)"}}>
        <div key='0-0' style={{color: "#156082", fontSize: "26px", fontFamily: "Aptos", textAlign: "left"}}>Title here</div>
      </div>
      <div key='1' style={{position: "absolute", left: "64.60750252283464px", top: "158.1768224047244px", width: "81.31958672677165px", height: "32.3124651503937px", transform: "rotate(0deg)"}}>
        <div key='1-0' style={{color: "#156082", fontSize: "14px", fontFamily: "Aptos", textAlign: "left"}}>Section</div>
      </div>
      <div key='3' style={{position: "absolute", left: "456.3027962480314px", top: "157.36674568976377px", width: "81.31958672677165px", height: "32.3124651503937px", transform: "rotate(0deg)"}}>
        <div key='3-0' style={{color: "#156082", fontSize: "14px", fontFamily: "Aptos", textAlign: "left"}}>Section</div>
      </div>
      <div key='4' style={{position: "absolute", left: "65.2151650456693px", top: "241.4170342511811px", width: "164.45670171811022px", height: "145.40593569685038px", transform: "rotate(0deg)"}}>
        <ul style={{ listStyleType: 'disc', paddingLeft: '20px', margin: 0 }}>
          <li key='0' style={{color: "#4ea72e", fontSize: "14px", fontFamily: "Aptos", marginLeft: "0px"}}>Bullet points</li>
          <li key='1' style={{color: "#4ea72e", fontSize: "14px", fontFamily: "Aptos", marginLeft: "20px"}}>Indent 1</li>
          <li key='2' style={{color: "#4ea72e", fontSize: "14px", fontFamily: "Aptos", marginLeft: "20px"}}>Indent 2</li>
          <li key='3' style={{color: "#4ea72e", fontSize: "14px", fontFamily: "Aptos", fontWeight: "bold", marginLeft: "0px"}}>Bullet points</li>
          <li key='4' style={{color: "#156082", fontSize: "14px", fontFamily: "Aptos", fontStyle: "italic", marginLeft: "0px"}}>Bullet points</li>
        </ul>
      </div>
      <div key='5' style={{position: "absolute", left: "683.4268478590551px", top: "306.2849035771653px", width: "484.5702321409449px", height: "62.857060704724404px", transform: "rotate(0deg)", backgroundColor: "#156082"}}>
        <div key='5-0' style={{color: "#ffffff", fontSize: "18px", fontFamily: "Aptos", textAlign: "center", display: "flex", alignItems: "center", justifyContent: "center", height: "100%"}}>Header text</div>
      </div>
      <div key='6' style={{position: "absolute", left: "297.1421442818897px", top: "511.99871999999993px", width: "158.85671571811022px", height: "60.57129214094488px", transform: "rotate(0deg)", clipPath: "polygon(0% 20%, 75% 20%, 75% 0%, 100% 50%, 75% 100%, 75% 80%, 0% 80%)", backgroundColor: "#E97032"}}>
      </div>
    </div>
  );
};

export default SlideComponent;