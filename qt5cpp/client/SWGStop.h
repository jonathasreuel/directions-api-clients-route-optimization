/**
 * Route Optimization API
 * Our Route Optimization API solves the so called vehicle routing problem fast. It calculates an optimal tour for a set of vehicles, services and constraints
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

/*
 * SWGStop.h
 * 
 * 
 */

#ifndef SWGStop_H_
#define SWGStop_H_

#include <QJsonObject>


#include "SWGAddress.h"
#include "SWGTimeWindow.h"
#include <QList>

#include "SWGObject.h"


namespace Swagger {

class SWGStop: public SWGObject {
public:
    SWGStop();
    SWGStop(QString* json);
    virtual ~SWGStop();
    void init();
    void cleanup();

    QString asJson ();
    QJsonObject* asJsonObject();
    void fromJsonObject(QJsonObject &json);
    SWGStop* fromJson(QString &jsonString);

    SWGAddress* getAddress();
    void setAddress(SWGAddress* address);

    qint64 getDuration();
    void setDuration(qint64 duration);

    QList<SWGTimeWindow*>* getTimeWindows();
    void setTimeWindows(QList<SWGTimeWindow*>* time_windows);


private:
    SWGAddress* address;
    qint64 duration;
    QList<SWGTimeWindow*>* time_windows;
};

} /* namespace Swagger */

#endif /* SWGStop_H_ */
